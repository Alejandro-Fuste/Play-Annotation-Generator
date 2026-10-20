# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_3`
- **Input XML**: `output_showcase/FieldGoalBlock/FieldGoalBlock_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-77] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-71] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-49] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-77] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [67-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-108] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-36] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [4-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [30-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [36-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [40-52] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [63-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [73-85] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [87-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-22] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-34] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-42] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-52] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-58] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-120] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-48] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-120] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-99] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-74] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '27' has 2 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.