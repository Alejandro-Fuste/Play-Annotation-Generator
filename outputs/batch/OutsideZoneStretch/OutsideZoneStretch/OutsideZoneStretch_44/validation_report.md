# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_44`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 133 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 90: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [0-371] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-402] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [204-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-267] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [305-336] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-419] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-257] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-347] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-248] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-309] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-339] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-316] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-332] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '17' starts at frame 204, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [204-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-271] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-411] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [204-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-277] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-294] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-135] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-243] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-266] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-278] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-325] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-53] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-60] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-82] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-297] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-271] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-342] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-187] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-215] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-236] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-241] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-256] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-245] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-256] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-286] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-307] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-327] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-292] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-325] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-284] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-291] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-302] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-291] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-279] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-419] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-352] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-364] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-327] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-357] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-366] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-382] for track '48' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.