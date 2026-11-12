# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_129`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [114–128], lower_priority='Action_ZoneBlock' annotated_start=117, effective_Action_ZoneBlock_start=129.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 141 frames exceeds threshold 90 frames [start=117, end=257].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 155 frames exceeds threshold 90 frames [start=117, end=271].
> - Action 'Action_None' range [114-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-329] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-308] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-329] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [142-240] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [243-296] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-264] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-271] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [120-260] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [264-271] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-280] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-303] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-321] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-246] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-256] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-272] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-329] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-309] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-328] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-256] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-311] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [316-321] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-236] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-276] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-261] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-271] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-311] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-317] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-250] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-282] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-304] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-329] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-308] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-271] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-317] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-252] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [254-257] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-255] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [258-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [269-270] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-95] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-208] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-280] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-329] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-329] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-314] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-319] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '31' has 1 frames without a visible bounding box.
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