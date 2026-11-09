# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_49`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 100: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=108, end=88. Clamping end to start.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-225] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-60] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-179] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-207] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-206] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-217] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-28] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-78] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-146] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-125] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-138] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-184] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-188] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '31' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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