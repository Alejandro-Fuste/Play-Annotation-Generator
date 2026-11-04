# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_2`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 48 |
| Player Tracks | 48 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 143 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 6: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 6: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Segment 'Action_CrossGoalLine' for track '21' has invalid range: start=570, end=569. Clamping end to start.
> - Action 'Action_None' range [8-235] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-57] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-69] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-569] for track '1' has 9 frames without a visible bounding box.
> - Action 'Action_None' range [8-116] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-150] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-224] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [231-293] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-384] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-523] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-527] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-533] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-178] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-300] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-138] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-279] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [8-167] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-569] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-569] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-569] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-318] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-257] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-286] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [8-32] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [56-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-109] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-318] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [322-569] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-200] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-339] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [345-566] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-248] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-283] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-305] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-278] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-243] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-309] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-318] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-248] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-277] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-28] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-158] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_CatchKick' range [171-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [200-569] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-104] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-100] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-158] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-276] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-294] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-303] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-280] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-288] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-311] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-547] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [550-552] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-393] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [289-547] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-336] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-471] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-405] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [426-427] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-455] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-469] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-483] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-493] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-493] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-550] for track '47' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Action event 'Action_CrossGoalLine' has invalid start frame 570. Video range is [0, 569].

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.