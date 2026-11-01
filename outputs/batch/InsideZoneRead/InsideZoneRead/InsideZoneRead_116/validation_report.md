# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_116`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_116/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 689 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=543, end=74. Clamping end to start.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [541–555], lower_priority='Action_ZoneBlock' annotated_start=543, effective_Action_ZoneBlock_start=556.
> - Action 'Action_PreSnap' range [0-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-540] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-685] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-568] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [576-594] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [600-624] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-640] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [648-677] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-432] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-620] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [635-644] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [648-671] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [673-674] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [676-681] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-638] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [649-653] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-363] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-548] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [555-556] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [558-569] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-405] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-540] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' for track '7' starts at frame 568, but the player has no visible bounding box on this frame.
> - Action 'Action_Handoff' range [568-568] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-618] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-635] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [637-648] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [654-656] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [662-664] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-397] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-404] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-633] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [638-652] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [543-574] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-625] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [627-689] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-542] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [543-555] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [568-605] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [607-608] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [610-622] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-634] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-652] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-445] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [543-559] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-364] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-388] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [541-594] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [613-618] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-623] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-689] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-130] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-262] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-374] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-397] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [541-611] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-370] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-374] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-365] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-371] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-660] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-546] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-569] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-581] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-585] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-571] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-620] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [610-662] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-627] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [629-630] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [626-657] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [678-689] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.