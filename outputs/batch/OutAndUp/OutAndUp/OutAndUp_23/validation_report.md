# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_23`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [11–17], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=18.
> - Action 'Action_RunGoRoute' range [120-152] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [154-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [164-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [178-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [214-219] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-66] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-152] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-185] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-229] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-38] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-64] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-143] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-174] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [11-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-48] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-207] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-80] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-55] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-26] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-67] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-146] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-218] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-39] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-65] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-135] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-226] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-141] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-121] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-187] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-176] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-193] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-192] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-223] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.