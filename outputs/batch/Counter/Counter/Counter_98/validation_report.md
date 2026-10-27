# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_98`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Overlapping action conflict at frame 192 for track '5': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
> - Action 'Action_DownBlock' range [192-248] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-282] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-345] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-312] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-371] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-270] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-338] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [192-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-389] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-334] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-379] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-233] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-295] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-339] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-243] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-263] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-242] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-34] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-275] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-284] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-321] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-389] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-250] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-270] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-327] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-344] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-373] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-342] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-356] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '29' has 1 frames without a visible bounding box.
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