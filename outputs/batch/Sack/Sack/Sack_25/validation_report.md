# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_25`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 52: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [84-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-62] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-82] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-89] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-84] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-90] for track '24' has 2 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.