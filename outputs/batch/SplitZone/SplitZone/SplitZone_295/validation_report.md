# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_295`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_295/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [79-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [42-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-43] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-104] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-137] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-41] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-96] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-140] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_Handoff' range [51-53] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [55-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-19] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-106] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [37-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [57-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-101] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-198] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [61-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-128] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-105] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-229] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.