# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_92`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 148 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 186: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [108-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-320] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-381] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-450] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-556] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [580-582] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-394] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-399] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-474] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-420] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-452] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-476] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-485] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-500] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-531] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [534-629] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-177] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-168] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-412] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-460] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [466-467] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-442] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [444-629] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-376] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [379-383] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-629] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-141] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-497] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-273] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-629] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-457] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-553] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-388] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-415] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-455] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-355] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-629] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-372] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-509] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [512-609] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-620] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-433] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-629] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-204] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-330] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-391] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-520] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [525-528] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-223] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-466] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-482] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-558] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-561] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-581] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [588-629] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-238] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-465] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [285-342] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [224-294] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-515] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-397] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-363] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-401] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-427] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-435] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-449] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-456] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-629] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-509] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-433] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-442] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-588] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [477-478] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-485] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-496] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-544] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-629] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [544-553] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-569] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-577] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-558] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [572-573] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-577] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-580] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [598-601] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [602-629] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-613] for track '51' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.