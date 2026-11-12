# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_230`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_230/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 37 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 97 frames exceeds threshold 90 frames [start=182, end=278].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [179–183], lower_priority='Action_ZoneBlock' annotated_start=182, effective_Action_ZoneBlock_start=184.
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 116 frames exceeds threshold 90 frames [start=182, end=297].
> - Segment 'Action_ZoneBlock' for track '16' has invalid range: start=182, end=52. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 116 frames exceeds threshold 90 frames [start=182, end=297].
> - Action 'Action_None' range [179-275] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-51] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-264] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [193-297] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-296] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-307] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [232-241] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [252-345] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-273] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-251] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-286] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-350] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-329] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-359] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' for track '12' starts at frame 179, but the player has no visible bounding box on this frame.
> - Action 'Action_SnapReceive' range [179-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [247-278] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-230] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-285] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-322] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-317] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-359] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-353] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-339] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-335] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-355] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-359] for track '37' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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