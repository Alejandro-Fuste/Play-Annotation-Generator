# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_33`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 71 |
| Player Tracks | 71 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 175 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 48: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ThrowPass' for track '11' has invalid range: start=93, end=74. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [12–26], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=27.
> - Action 'Action_RunGoRoute' range [76-269] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-201] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-227] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-28] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-33] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-47] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-227] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [12-74] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-102] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-112] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-218] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-104] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-218] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-69] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-116] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-48] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [12-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-20] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-47] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-58] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-106] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-194] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-105] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-104] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-145] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-194] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-143] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-168] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-203] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-141] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-182] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-141] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-147] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-167] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-187] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-246] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-188] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-176] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-201] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '43' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-227] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-198] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-218] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-227] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-269] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-246] for track '64' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-269] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '70' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.
> - Player track '69' has undefined position. Will map to Position_Unknown.
> - Player track '69' has undefined team_side. Will map to Team_Unknown.
> - Player track '70' has undefined position. Will map to Position_Unknown.
> - Player track '70' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.