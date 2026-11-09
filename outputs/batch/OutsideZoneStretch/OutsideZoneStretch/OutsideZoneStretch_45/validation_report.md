# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_45`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 92: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [102-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-238] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-19] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [82-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [121-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-76] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-223] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-224] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-235] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-245] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-243] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-241] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-261] for track '35' has 2 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.