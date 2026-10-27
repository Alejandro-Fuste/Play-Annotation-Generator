# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_192`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_192/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 386: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 386: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [99-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [104-134] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [136-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-233] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [140-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [143-268] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [104-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-140] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-269] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-258] for track '21' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.