# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_119`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_119/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 140 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_BallCarry' for track '11' has invalid range: start=138, end=123. Clamping end to start.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [99–114], lower_priority='Action_ZoneBlock' annotated_start=101, effective_Action_ZoneBlock_start=115.
> - Action 'Action_None' range [99-234] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-186] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-240] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-183] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-231] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-140] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-215] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-251] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-143] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-209] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-45] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-178] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-257] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-29] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-121] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-255] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-174] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-219] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-245] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-65] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-72] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-97] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-111] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-119] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-94] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-159] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-203] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-147] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-269] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-166] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-169] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-179] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-253] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-269] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [198-227] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-227] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-243] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-264] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-250] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '42' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.