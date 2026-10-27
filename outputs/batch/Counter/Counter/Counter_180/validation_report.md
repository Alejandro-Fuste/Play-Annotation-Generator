# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_180`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_180/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 362: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BallCarry' for track '3' has invalid range: start=148, end=140. Clamping end to start.
> - Action 'Action_None' range [105-161] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [107-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [129-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [112-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [125-140] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [105-173] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [107-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [129-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [147-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [174-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-286] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-254] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-209] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-263] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-93] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-156] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-273] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.