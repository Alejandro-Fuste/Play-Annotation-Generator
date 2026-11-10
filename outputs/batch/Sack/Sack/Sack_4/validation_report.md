# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_4`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 42 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_SackQuarterback' for track '0' has invalid range: start=300, end=299. Clamping end to start.
> - Segment 'Action_SackQuarterback' for track '5' has invalid range: start=300, end=299. Clamping end to start.
> - Action 'Action_PreSnap' range [0-295] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [282-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-291] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-275] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-283] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-295] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-112] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-256] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-279] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '20' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Action event 'Action_SackQuarterback' has invalid start frame 300. Video range is [0, 299].
> - Action event 'Action_SackQuarterback' has invalid start frame 300. Video range is [0, 299].

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.