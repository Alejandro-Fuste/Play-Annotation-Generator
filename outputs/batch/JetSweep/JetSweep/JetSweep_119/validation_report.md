# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_119`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_119/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [43–58], lower_priority='Action_ZoneBlock' annotated_start=44, effective_Action_ZoneBlock_start=59.
> - Action 'Action_None' range [43-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-130] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [44-67] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [43-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [90-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-192] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [67-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [216-218] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-229] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-201] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-222] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.