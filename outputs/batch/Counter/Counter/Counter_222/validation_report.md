# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_222`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_222/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 58 |
| Player Tracks | 58 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 446: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 446: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 446: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [259–276], lower_priority='Action_DownBlock' annotated_start=263, effective_Action_DownBlock_start=277.
> - Action 'Action_None' range [259-312] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-494] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [263-305] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-408] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-420] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-324] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-324] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-323] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-346] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-331] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-453] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [263-326] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 327, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [327-399] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-469] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-320] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-343] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-327] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-397] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-433] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-440] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-457] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [277-308] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-337] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-308] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-324] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-304] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-340] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-335] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [341-415] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [270-271] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-328] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-337] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-312] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-457] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-425] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-324] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-345] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-407] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-379] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-569] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-569] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-399] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [407-476] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [493-496] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-399] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-479] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-505] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-397] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-417] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-451] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [453-486] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-432] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-466] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-532] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-529] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-462] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-541] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-524] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-442] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-451] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-468] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [456-512] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-494] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-479] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-541] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-564] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [537-541] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-564] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-539] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-539] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-569] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-545] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-564] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-557] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [560-564] for track '54' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [555-557] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-562] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-564] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-569] for track '57' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.