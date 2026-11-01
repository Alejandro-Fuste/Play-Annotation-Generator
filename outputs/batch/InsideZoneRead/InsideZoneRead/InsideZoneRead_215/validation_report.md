# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_215`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_215/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [96–114], lower_priority='Action_ZoneBlock' annotated_start=99, effective_Action_ZoneBlock_start=115.
> - Segment 'Action_SnapReceive' for track '13' has invalid range: start=124, end=114. Clamping end to start.
> - Segment 'Action_BallCarry' for track '13' has invalid range: start=145, end=129. Clamping end to start.
> - Action 'Action_None' range [96-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-175] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-212] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-189] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-162] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-198] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-129] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '10' starts at frame 99, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [99-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-141] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [142-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [165-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [124-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-240] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-260] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-285] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-290] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-274] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-212] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-299] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-276] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-245] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-281] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-277] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '27' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.