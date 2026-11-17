# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_264`
- **Input XML**: `outputs/batch/Power/Power/Power_264/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 528: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [20-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-144] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-76] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-144] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-206] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-126] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-176] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-235] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-141] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-257] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-125] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-132] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-86] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '13' starts at frame 89, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [89-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [114-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-77] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [89-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [128-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-124] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-115] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-251] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-163] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-184] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-222] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-247] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-220] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-251] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-235] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-211] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-245] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-229] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-234] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-269] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-265] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-252] for track '37' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.