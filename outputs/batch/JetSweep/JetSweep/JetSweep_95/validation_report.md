# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_95`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 55 |
| Player Tracks | 55 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 136 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=83, end=23. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '15' has invalid range: start=85, end=23. Clamping end to start.
> - Segment 'Action_BallCarry' for track '18' has invalid range: start=112, end=93. Clamping end to start.
> - Action 'Action_None' range [83-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-246] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-268] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-235] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-291] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-305] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-317] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-333] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-256] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-132] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-294] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-173] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_Toss' range [102-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-141] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-208] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-23] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [88-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [105-113] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [116-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-389] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-136] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-264] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-284] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-136] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-311] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-153] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-169] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-192] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-181] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-318] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-232] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-271] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-254] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-290] for track '35' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [297-353] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-379] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-284] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-287] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-389] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-322] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-367] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-294] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-348] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [357-363] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-369] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-345] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-288] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-301] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-314] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-353] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-367] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-361] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-383] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-378] for track '53' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.