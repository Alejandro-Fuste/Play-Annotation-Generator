# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_64`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [48-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-122] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-95] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [52-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-87] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-119] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-79] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-20] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-109] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-87] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-104] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '27' has 2 frames without a visible bounding box.
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