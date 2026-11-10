# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_131`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_131/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 31 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [160-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [152-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '24' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.