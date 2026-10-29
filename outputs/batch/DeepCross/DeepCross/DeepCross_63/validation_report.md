# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_63`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 66: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 66: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 66: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 66: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [17-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-104] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-134] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-141] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-194] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-143] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-143] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-141] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-173] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-201] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-143] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-85] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-147] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [172-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [207-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-47] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-174] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-106] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [32-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [91-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-101] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [120-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [156-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [188-199] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-134] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-143] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-188] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-192] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '43' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.