# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_96`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_96/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [0-294] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-321] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-259] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-309] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-187] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-259] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-294] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-294] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-294] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [157-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-294] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' for track '14' starts at frame 141, but the player has no visible bounding box on this frame.
> - Action 'Action_PressEdge' range [141-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-302] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-256] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-294] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-237] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [140-184] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-247] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-231] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-237] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-182] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-294] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-412] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-302] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-379] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-388] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-392] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-405] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-302] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-383] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-336] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-302] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-302] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-321] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-320] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-319] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-310] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-385] for track '44' has 1 frames without a visible bounding box.
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