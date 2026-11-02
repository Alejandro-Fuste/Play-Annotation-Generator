# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_152`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_152/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [76–89], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=90.
> - Segment 'Action_BallCarry' for track '17' has invalid range: start=98, end=85. Clamping end to start.
> - Action 'Action_ZoneBlock' range [78-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-236] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-241] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-129] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [70-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-224] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-249] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-262] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-243] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-240] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-258] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-269] for track '31' has 2 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.