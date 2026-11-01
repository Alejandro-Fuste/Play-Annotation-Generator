# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_234`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_234/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [122–134], lower_priority='Action_ZoneBlock' annotated_start=125, effective_Action_ZoneBlock_start=135.
> - Action 'Action_ZoneBlock' range [125-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [148-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [161-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-30] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-253] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '19' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.