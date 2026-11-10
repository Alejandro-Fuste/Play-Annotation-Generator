# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_96`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_96/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
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
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [77-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [55-72] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [78-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-46] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-66] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '21' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.