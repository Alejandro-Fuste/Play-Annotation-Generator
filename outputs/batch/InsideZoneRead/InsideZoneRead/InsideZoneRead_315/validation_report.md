# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_315`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_315/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 219 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [14–27], lower_priority='Action_ZoneBlock' annotated_start=17, effective_Action_ZoneBlock_start=28.
> - Action 'Action_None' range [14-112] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-147] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-130] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-199] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-91] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-214] for track '4' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [14-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-144] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-130] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-153] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-190] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-231] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-143] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-162] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-193] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-43] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-139] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-222] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-169] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-216] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [14-179] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-77] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-84] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-133] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-133] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-214] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-84] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-91] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-162] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-127] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_Keep' range [39-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [62-84] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-89] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [102-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-133] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-163] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-239] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [66-87] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-133] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [95-113] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [125-163] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-236] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [121-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-187] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-217] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-225] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-219] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-190] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-239] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-218] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '50' has 1 frames without a visible bounding box.
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