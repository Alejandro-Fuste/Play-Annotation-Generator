# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_303`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_303/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [59–72], lower_priority='Action_DownBlock' annotated_start=62, effective_Action_DownBlock_start=73.
> - Action 'Action_None' range [59-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-165] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [62-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [130-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-218] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-239] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-114] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-222] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-223] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-112] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-72] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-124] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.