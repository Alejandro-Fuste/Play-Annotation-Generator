# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_380`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_380/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 142 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [3–19], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=20.
> - Action 'Action_None' range [3-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-223] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-81] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-201] for track '3' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [203-253] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-44] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-88] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-107] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [52-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [228-234] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [241-243] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-11] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-4] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-12] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-60] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-246] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [35-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-92] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-242] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-205] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-225] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-181] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-225] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-247] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-249] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-201] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-143] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-161] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-183] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-201] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-171] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-186] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-226] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-246] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-260] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-204] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-218] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-228] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-256] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-265] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-269] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.