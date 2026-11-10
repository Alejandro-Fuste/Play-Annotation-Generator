# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_145`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_145/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-10] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-86] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-85] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [39-71] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [76-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [80-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-36] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-90] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-90] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '23' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.