# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_351`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_351/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 704: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [81–94], lower_priority='Action_DownBlock' annotated_start=84, effective_Action_DownBlock_start=95.
> - Action 'Action_None' range [81-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [125-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [154-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [106-124] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-189] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-191] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-122] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-184] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [84-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [84-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-211] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-70] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [121-153] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-186] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '29' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.