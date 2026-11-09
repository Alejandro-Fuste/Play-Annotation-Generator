# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_151`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 14 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 304: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-217] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-267] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-345] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-357] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-313] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-326] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-147] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-198] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-356] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-340] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [137-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-319] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-291] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-327] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-340] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-351] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-359] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.