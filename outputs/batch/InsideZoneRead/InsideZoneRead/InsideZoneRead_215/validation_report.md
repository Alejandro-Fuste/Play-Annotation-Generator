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
| CSV events parsed | 17 |
| Action Segments inferred | 74 |
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
> - Segment 'Action_SnapReceive' for track '15' has invalid range: start=150, end=61. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '15' has invalid range: start=150, end=100. Clamping end to start.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=169, end=61. Clamping end to start.
> - Action 'Action_None' range [46-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-175] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-212] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-189] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [195-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-162] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [164-299] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-198] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 46, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [46-77] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-83] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-129] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-240] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [242-260] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [271-285] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-290] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '17' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_215'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.