# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_6`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 201 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [16-54] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-206] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-238] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-225] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-266] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-62] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-76] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [77-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [92-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-246] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-114] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-207] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [16-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-53] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-50] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-386] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-390] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-419] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-59] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-195] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-332] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-350] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [356-361] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-384] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-78] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-104] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-404] for track '11' has 6 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [16-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-52] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-225] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-270] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CatchPunt' range [192-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-215] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-250] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 16, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [16-173] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-337] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [340-376] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-48] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-9] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-48] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-28] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-297] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [300-307] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-325] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-335] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-343] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-205] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-214] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [220-226] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-278] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-283] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [377-380] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-402] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-104] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-301] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-131] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-255] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-344] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-187] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-205] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-295] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_Tackle' range [318-321] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-188] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-306] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-345] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-352] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-175] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-191] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-264] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-354] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [357-419] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-207] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-297] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-330] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-340] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-373] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [383-389] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-398] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-260] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-295] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-305] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-320] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-324] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-350] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-281] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-298] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-330] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-396] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-290] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-292] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-372] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-320] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-370] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-396] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-412] for track '48' has 2 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.