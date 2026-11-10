# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_38`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 159 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [41-124] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-138] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-124] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-110] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-119] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-136] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [86-101] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-191] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-214] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-228] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [86-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-140] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [144-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-197] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [86-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-161] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-124] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-124] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [95-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [99-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-196] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-206] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-237] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-214] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-219] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-235] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-227] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-237] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '50' has 1 frames without a visible bounding box.
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