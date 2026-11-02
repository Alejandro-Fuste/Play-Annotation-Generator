# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_212`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_212/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 129 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 426: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Resolved action overlap for track '0' (C): higher_priority='Action_BallSnap' [213–227], lower_priority='Action_ZoneBlock' annotated_start=216, effective_Action_ZoneBlock_start=228.
> - Action 'Action_ZoneBlock' range [228-275] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-501] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-251] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-260] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-284] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-490] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [216-259] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [261-266] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [268-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-283] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-244] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-277] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-469] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [216-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-385] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-534] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-539] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-600] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-226] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-437] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [439-629] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-259] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-355] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-495] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [501-518] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [520-542] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-546] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [212-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [242-402] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-293] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-305] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-472] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [474-476] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-484] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-491] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-564] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-367] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-464] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-378] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [381-384] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-396] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-415] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [417-486] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-493] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [495-497] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-501] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-504] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-512] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-486] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-377] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-414] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-396] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-520] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-531] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-576] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [583-613] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-506] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-529] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-443] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-448] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-483] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [429-443] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [450-605] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-434] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-441] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [431-438] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-456] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-554] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-472] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-493] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [442-453] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-497] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-605] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [445-500] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [454-610] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [460-505] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-534] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-547] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [549-620] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-595] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [527-579] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [602-604] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [606-620] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [622-629] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-612] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [619-623] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [619-629] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [625-628] for track '49' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.