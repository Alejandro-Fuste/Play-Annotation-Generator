# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_81`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_81/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [0-405] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-284] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-346] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-419] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-385] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-386] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-153] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [115-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-266] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-366] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-151] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-275] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-381] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-283] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-129] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-217] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-225] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-309] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-319] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-355] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-363] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-176] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-255] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-264] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-283] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-294] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-309] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-341] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-358] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-278] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-282] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-296] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-287] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-302] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-320] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-332] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-317] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-332] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-358] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-366] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-371] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-389] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-402] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-351] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-362] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-393] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-398] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-401] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-411] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-402] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-405] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-419] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-400] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-396] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-415] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-400] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-410] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-419] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-410] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-418] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.