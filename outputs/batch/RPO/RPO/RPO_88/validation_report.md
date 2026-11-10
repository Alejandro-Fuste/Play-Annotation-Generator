# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_88`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 162: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-184] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-190] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-233] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-199] for track '2' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-164] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-199] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-204] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-220] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-217] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-132] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-205] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-218] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-214] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-159] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-183] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-163] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-185] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-198] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-128] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-151] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-225] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '33' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.