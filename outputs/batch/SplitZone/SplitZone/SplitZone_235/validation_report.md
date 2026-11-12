# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_235`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_235/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 100 frames exceeds threshold 90 frames [start=144, end=243].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 100 frames exceeds threshold 90 frames [start=144, end=243].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [141–157], lower_priority='Action_ZoneBlock' annotated_start=144, effective_Action_ZoneBlock_start=158.
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 91 frames exceeds threshold 90 frames [start=144, end=234].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 100 frames exceeds threshold 90 frames [start=144, end=243].
> - Action 'Action_SplitBlock' range [160-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-298] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-284] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [171-282] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [284-329] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-243] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-291] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 244, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [244-325] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-234] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-328] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-277] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-140] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-207] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-277] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-17] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [182-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-28] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-27] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-234] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-284] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-327] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-305] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-261] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-299] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-312] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-326] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-326] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-324] for track '36' has 2 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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