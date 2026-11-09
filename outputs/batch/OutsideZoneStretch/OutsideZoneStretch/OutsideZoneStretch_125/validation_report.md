# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_125`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-317] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-226] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-303] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 171, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [171-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-238] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-265] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-328] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-142] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-311] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-66] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-230] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-293] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-303] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-322] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-277] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-288] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-319] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-294] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-301] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-327] for track '30' has 1 frames without a visible bounding box.
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