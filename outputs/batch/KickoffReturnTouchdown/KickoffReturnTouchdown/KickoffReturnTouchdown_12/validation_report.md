# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_12`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 62 |
| Player Tracks | 62 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 220 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 26: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action 'Action_None' range [58-72] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-141] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-199] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-335] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [341-402] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [405-407] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-496] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-417] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-465] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-426] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-482] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-327] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_KickBall' range [112-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-273] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-314] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-403] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-482] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-93] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-388] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-394] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-403] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-410] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-444] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [451-509] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-301] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [349-372] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [378-388] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [395-406] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-247] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-164] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-248] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-374] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-463] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-266] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-305] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-317] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-272] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-352] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-203] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-250] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-432] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-114] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-282] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-433] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-119] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-137] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-324] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-336] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-477] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-135] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-135] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-277] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-289] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-531] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [533-557] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-569] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-8] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-18] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-57] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-311] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-64] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-319] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-105] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-409] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-418] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-191] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-370] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-471] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-197] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [239-240] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [242-243] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-300] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-209] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-236] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-419] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-470] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-569] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-310] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-323] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-338] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-380] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-566] for track '44' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [337-385] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-403] for track '45' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [410-411] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-419] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-457] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-359] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-369] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-382] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-390] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-442] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-446] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-383] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-490] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-377] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-458] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-518] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [526-569] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-398] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-400] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-421] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-455] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [461-463] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-467] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-519] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-559] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [561-563] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-569] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [528-533] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-535] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-540] for track '61' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.