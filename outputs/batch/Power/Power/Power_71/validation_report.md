# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_71`
- **Input XML**: `outputs/batch/Power/Power/Power_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 159 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 144: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 144: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action 'Action_PreSnap' range [24-482] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-561] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-511] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [518-520] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [527-556] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-485] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-515] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-567] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [574-578] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-485] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-529] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [565-582] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-456] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [461-466] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [472-474] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-485] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-489] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [491-514] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-475] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [477-482] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-611] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [616-626] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-626] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-509] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [515-569] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-42] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-78] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-87] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-34] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-141] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-255] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-294] for track '12' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-306] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-428] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [429-442] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-485] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [487-489] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-155] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-188] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-197] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-464] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [466-478] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-485] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-599] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [604-607] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-559] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [594-599] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-482] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-517] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-548] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-98] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-148] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-154] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-182] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-480] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [483-485] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-489] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [491-535] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [541-554] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-60] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-80] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-548] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-218] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-236] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-463] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [466-478] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [491-527] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-236] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-428] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [429-436] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [439-459] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-466] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-218] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-255] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-270] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-280] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-428] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-479] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-485] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-428] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [429-436] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [440-444] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [446-457] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-479] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-485] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-557] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [450-451] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [454-457] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [483-485] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-502] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [488-489] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [492-507] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [513-550] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [494-495] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [523-529] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [548-559] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [561-580] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [530-591] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [575-576] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [578-624] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [590-613] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [603-605] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [607-629] for track '38' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.