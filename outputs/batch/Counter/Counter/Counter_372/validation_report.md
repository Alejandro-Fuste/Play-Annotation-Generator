# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_372`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_372/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 67 |
| Player Tracks | 66 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 148 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [116–129], lower_priority='Action_PullBlock' annotated_start=119, effective_Action_PullBlock_start=130.
> - Action 'Action_None' range [116-240] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-255] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [119-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-190] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-434] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-442] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-445] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-40] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [130-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [119-156] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 157, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [157-157] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [201-265] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-217] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-253] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-201] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-280] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-182] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-277] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-246] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-318] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-270] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-346] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-353] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-364] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-375] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-382] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-417] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-429] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [433-437] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-449] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-242] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-295] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-305] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-308] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-307] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-311] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-332] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-343] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-353] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-329] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-373] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-332] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-358] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-362] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-334] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-337] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-367] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-375] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-345] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-347] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-371] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-399] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-365] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-378] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-355] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-373] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-377] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-392] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-381] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-386] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-415] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [414-415] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-419] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-426] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-426] for track '61' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [423-427] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-425] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-447] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-430] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-435] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-448] for track '66' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.