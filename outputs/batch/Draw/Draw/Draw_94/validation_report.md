# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_94`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 206 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [31–44], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=45.
> - Action 'Action_None' range [31-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-251] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-284] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-330] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-337] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-361] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-368] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-390] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-419] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-419] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-402] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-216] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-227] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-144] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-250] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-266] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-274] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-300] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-352] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-366] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-266] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-283] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [291-300] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-358] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-390] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-396] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-406] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-418] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-266] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-300] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-306] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-376] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [378-388] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-406] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-246] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-297] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-120] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-419] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-202] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-74] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-124] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-246] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [81-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-118] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [126-218] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [221-248] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-363] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-370] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-241] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-209] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-234] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-284] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-221] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-275] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [277-300] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-312] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-367] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-417] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-386] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-247] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-393] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-400] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-246] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-312] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-354] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-373] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-410] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-246] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-265] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-288] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-352] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-286] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-295] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-396] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [401-418] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-287] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-297] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [299-302] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-326] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-419] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-395] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-413] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-321] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-336] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-371] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-417] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-416] for track '40' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [372-375] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-386] for track '41' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [388-393] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-419] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-404] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-410] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-416] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-416] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.