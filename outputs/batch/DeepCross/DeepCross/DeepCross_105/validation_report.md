# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_105`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_105/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ThrowPass' for track '13' has invalid range: start=109, end=66. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [1–13], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=14.
> - Action 'Action_None' range [1-48] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-134] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-206] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-35] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-32] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-40] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-59] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-93] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-130] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-153] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-62] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-100] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [182-183] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-6] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-28] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [37-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [140-161] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [163-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-77] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-166] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-115] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-151] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-200] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-196] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-188] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '39' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.