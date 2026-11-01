# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_114`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 230: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 230: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 99 frames exceeds threshold 90 frames [start=114, end=212].
> - Segment 'Action_BallSnap' for track '12' has invalid range: start=111, end=36. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '12' has invalid range: start=114, end=36. Clamping end to start.
> - Action 'Action_None' range [111-249] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-321] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-351] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-296] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-303] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-364] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-158] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 111, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [111-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-176] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-281] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-73] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-174] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-226] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-17] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-240] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-273] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-158] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-305] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-313] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-376] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-289] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-296] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-317] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-342] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-385] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-361] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-330] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-353] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-373] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-338] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-357] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-325] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-353] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-361] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-347] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-360] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-381] for track '36' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.