# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_44`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [26–41], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=42.
> - Segment 'Action_ZoneBlock' for track '14' has invalid range: start=29, end=25. Clamping end to start.
> - Action 'Action_None' range [26-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-102] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-264] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-228] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-262] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-89] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-161] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 73, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [73-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 73, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [73-83] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-187] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-171] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-268] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-249] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-264] for track '30' has 1 frames without a visible bounding box.
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