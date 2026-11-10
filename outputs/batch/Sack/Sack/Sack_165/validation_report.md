# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_165`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_165/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 21 |
| Ball Tracks | 2 |
| CSV events parsed | 11 |
| Action Segments inferred | 34 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-116] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [144-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-150] for track '22' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.