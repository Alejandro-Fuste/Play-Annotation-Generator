# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_15`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [8–26], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=27.
> - Action 'Action_None' range [8-78] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-93] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-239] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [26-160] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [180-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-155] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-162] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-162] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-160] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-162] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [8-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [134-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-73] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-103] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-134] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-107] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-162] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-162] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-160] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-199] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-234] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-173] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-193] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-224] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-173] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-211] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-198] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-222] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-236] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-207] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-202] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-237] for track '50' has 2 frames without a visible bounding box.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.