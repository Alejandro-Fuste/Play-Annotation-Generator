# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_106`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [87–103], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=104.
> - Action 'Action_None' range [179-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-243] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-223] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-271] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-259] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [263-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-235] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-145] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-233] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-244] for track '12' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [246-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-280] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-246] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-294] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [87-98] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-246] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-288] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-249] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-207] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-271] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-284] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-293] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '29' has 2 frames without a visible bounding box.
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